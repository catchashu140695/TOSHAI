$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        }
    });   

    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync:true
        },
        out: {
            effect: "fadeOutUp",
            sync:true
        }
    });

    $('#MicBtn').click(function(){       
        
        $('#Oval').attr('hidden',true);
        $('#SiriWave').attr('hidden',false);
        eel.allCommand();

    });

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true,
        width: 800
    });


    function doc_keyup(e){
        if(e.key==="j" && e.metaKey){           
            $('#Oval').attr('hidden',true);
            $('#SiriWave').attr('hidden',false);
            eel.allCommand();
        }
    }
    document.addEventListener('keyup',doc_keyup,false);

});

