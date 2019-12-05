const fs = require('fs')

fs.readFile('SocialMediaData/twitter_ad-engagements.js', (err, data) => {
    if (err) throw err;

    console.log(data.toString());
})
