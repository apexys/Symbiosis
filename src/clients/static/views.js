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
        console.log("createChatSessionOverView!");
    }

    this.createChatView = function(chatID){

    }

    this.createAddChatView = function(){

    }

    this.createSettingsView = function(){

    }

    this.createNetworkOverView = function(){

    }

    this.createAddNetworkView = function(){

    }
}
