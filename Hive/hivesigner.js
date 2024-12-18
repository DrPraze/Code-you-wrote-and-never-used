const express = require("express");
const axios = require("axios");
const fs = require('fs').promises;
require("dotenv").config();

const router = express.Router();

const HIVE_AUTH_URL = "https://hivesigner.com/oauth2/authorize";
const HIVE_TOKEN_URL = "https://hivesigner.com/api/oauth2/token";
const rate = 1000;

// Step 1: Redirect user to Hivesigner authorization link
router.get("/login", (req, res) => {
    const HIVESIGNER_CLIENT_ID = "slakenet";
    const HIVESIGNER_REDIRECT_URI = "http://slakenet3.onrender.com/auth/callback";
    const scope = "login,vote,comment,active";

    const authUrl = `${HIVE_AUTH_URL}?client_id=${HIVESIGNER_CLIENT_ID}&redirect_uri=${HIVESIGNER_REDIRECT_URI}&scope=${scope}`;

    res.redirect(authUrl);
});

// Step 2: Handle callback and exchange code for access token

router.get('/callback', async (req, res) => {
  const { access_token, expires_in, username } = req.query;

  if (!access_token) {
    return res.status(400).json({ error: "Access token is missing" });
  }

  try {
    // Read and parse users.json
    const data = await fs.readFile('./data/users.json', 'utf8');
    const users = JSON.parse(data);

    // Validate the user
    const user = users[req.session.email];
    if (!user) {
      return res.status(404).json({ error: "User not found in database." });
    }

    // Fetch data from Hivesigner API
    const response = await axios.get("https://hivesigner.com/api/me", {
      headers: { Authorization: `Bearer ${access_token}` },
    });

    // Extract relevant data
    req.session.hivesignerConnected = true;
    req.session.hiveAccessToken = access_token;
    req.session.hiveTime = Date.now();

    const voting_mana = response.data.account.voting_power/100;
    const profileName = response.data.user_metadata.profile.name;
    const hiveBalance = response.data.account.balance;
    const profileImage = response.data.user_metadata.profile.profile_image;
    const about = response.data.user_metadata.profile.about;

    // If linked to Hivesigner
    if (req.session.hivesignerConnected) {
      const sortedAccounts = Object.keys(users).sort(
        (a, b) => users[b].balance - users[a].balance
      );
      const top5Usernames = sortedAccounts
        .slice(0, 5)
        .map(account => users[account]?.username || "Unknown");

      const [top1, top2, top3, top4, top5] = top5Usernames;
      const balance = user.balance;
      // Render the page
      return res.render('earn.ejs', {
        name: profileName,
        balance: balance.toFixed(3),
        email: req.session.email,
        rate: rate,
        voting_mana: voting_mana,
        hiveBalance: hiveBalance,
        profileImage: profileImage,
        about: about,
        top1,
        top2,
        top3,
        top4,
        top5,
      });
    } else {
      res.redirect('/channels');
    }
  } catch (error) {
    if (error.code === 'ENOENT') {
      console.error("users.json file not found:", error.message);
      return res.status(500).json({ error: "User data file missing." });
    } else if (error.response) {
      console.error("Hivesigner API Error:", error.response.data);
      return res.status(500).json({ error: "Failed to fetch user info from Hivesigner." });
    } else {
      console.error("Unexpected Error:", error.message);
      return res.status(500).json({ error: "An unexpected error occurred." });
    }
  }
});




module.exports = router;
