/*
function ViewGenerator(){
    this.clearView = function(){
        console.log("clearView!");
        document.getElementById('header-text').textContent = "";
        $('#content').children('div').attr('display', 'none');
    }

    this.createLoginView = function(){
        $('#header-text').text('Login');
        $('#login').attr('display', 'block');
    }

    this.createChatSessionOverView = function(){
        $('#header-text').text('Chat Sessions');
        $('#chat-sessions').attr('display', 'block');
    }

    this.createChatView = function(chatID){
        //Do some magic here
        var chatname = '#somechat';

        $('#header-text').text(chatname);
        $('#login').attr('display', 'block');
    }

    this.createAddChatView = function(){
        $('#header-text').text('Login');
        $('#login').attr('display', 'block');
    }

    this.createSettingsView = function(){
        $('#header-text').text('Login');
        $('#login').attr('display', 'block');
    }

    this.createNetworkOverView = function(){
        $('#header-text').text('Login');
        $('#login').attr('display', 'block');
    }

    this.createAddNetworkView = function(){
        $('#header-text').text('Login');
        $('#login').attr('display', 'block');
    }
}*/
function canIhazLogin() {
    useful.post("/login",
                {"username": "foo",
                 "password": "bar"},
                function(x){console.log(x.responseText);},
                function(x){console.log("ERROR AY")});
    }
