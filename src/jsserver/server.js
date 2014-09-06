var express = require('express');
var app = express();


var bodyParser = require('body-parser');

var cookieParser = require('cookie-parser');

var auth = require('./auth');

app.use(cookieParser());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

app.get('/', function (req, res) {
    if (!req.cookies.number) {
        res.cookie('number', 0);
        res.send('Cookie set');
    } else {
        var number = parseInt(req.cookies.number);
        res.cookie('number', number + 1);
        res.send('Number: ' + number);
    }
});

app.get('/login', function (req, res) {
    res.sendfile('./login.html');
});

app.post('/login', function (req, res) {
    if (auth.auth.authenticate(req, res)) {
        res.redirect('/upload');
    } else {
        res.redirect('/login');
    }
});

app.get('/upload', function (req, res) {
    if (!auth.auth.checkAuth(req, res)) {
        res.redirect('/login');
    } else {
        res.send("Upload!");
    }
});
var server = app.listen(3000, function () {
    console.log('Listening on port %d', server.address().port);
})
