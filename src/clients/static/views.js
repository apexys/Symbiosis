function ViewGenerator(){
    this.clearView = function(){
        console.log("clearView!");
        document.getElementById('header-text').textContent = "";
        $('#content').children('div').attr('display', 'block');
    }

    this.createLoginView = function(){
        document.getElementById('header-text').textContent = "Login";
        document.getElementById('content');

        document.getElementById('footer').innerHTML= "";

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
