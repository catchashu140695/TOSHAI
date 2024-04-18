$(document).ready(function(){

    eel.expose(DisplayMessage)
    function DisplayMessage(message){
        $('.siri-message').text(message)
        $('.siri-message').textillate('start')
    }

    eel.expose(showhood)
    function showhood(){
        $('#Oval').attr('hidden',false);
        $('#SiriWave').attr('hidden',true);
    }


});