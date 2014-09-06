
exports.auth = {

    authenticate: function (req, res) {
        var user = req.body.user;
        var password = req.body.password;
        var shasum = require('crypto').createHash('sha512');
        shasum.update(password);
        var hashed = shasum.digest('hex');

        if (this.logins.hasOwnProperty(user) && this.logins[user] == hashed) {
            console.log("Login with " + user + " and pw " + password + "succeeded!");
            return true;
        } else {
            console.log("Login with " + user + " and pw " + password + "failed!");
            return false;
        }
    },

    checkAuth: function (req, res) {

    },

    privateKey: "Stealing Keys is evil",

    logins: {
        "apexys": '0c61cffa91f98dbf3ab349d1fe276d31ff74c1456b7f770336cdc05b9889c669a78a6185c90f3007f3537edd306980b7f48e90ab51c821dbf7810664b824511e'
    }

}
