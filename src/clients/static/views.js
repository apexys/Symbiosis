function ViewGenerator(){
    this.clearView = function(){
        console.log("clearView!");
        document.getElementById('header-text').textContent = "";
        document.getElementById('content').innerHTML = "";
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
