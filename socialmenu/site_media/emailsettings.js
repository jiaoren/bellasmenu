$(document).ready(function(){
    
    $('label[for^="id_email"]').click(function(){
    	
    	if($(this).children('input[id^="id_email"]').is(':checked')){
    	    $(this).children('.switch').children(':first').attr({"class":"shadow"});
    	    $(this).children('.switch').children('.border').children('.knob').css('margin-left','0%');
    	    $(this).children('input[id^="id_email"]').prop("checked", false);
    	}else{
    		$(this).children('.switch').children(':first').attr({"class":"shadow on"});
    	    $(this).children('.switch').children('.border').children('.knob').css('margin-left','62%');
    	    $(this).children('input[id^="id_email"]').checked = true;
    	    $(this).children('input[id^="id_email"]').prop("checked", true);
    	}
    });
    
    
});
