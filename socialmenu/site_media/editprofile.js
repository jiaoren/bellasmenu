window.addEvent('domready', function() {

    var myFancySelect = new FancySelect('id_language', {
	    showText: true,
	    showImages: true,
	    autoHide:true,
	    className: 'FancySelect'
    });
});

$(document).ready(function(){
	
    $('.Button.WhiteButton.Button18.change_avatar').click(function(){
    	$(this).hide();
    	$("#id_img").show();
    });
    
    $('a[name="deactivate_user_account"]').click(function(){
    	$(this).hide();
    	$("#DeactivateForm").show();
    });
    $('#enable_button').prop("checked", false);
    href = $("#deactivate_user_account_confirm").attr("href");
    $("#deactivate_user_account_confirm").removeAttr("href");
    $('#enable_button').click(function(){
    	if($("#deactivate_user_account_confirm").hasClass('disabled')){
    		$("#deactivate_user_account_confirm").removeClass('disabled');
    		$("#deactivate_user_account_confirm").attr("href", href);
    	    
    	}else{
            $("#deactivate_user_account_confirm").addClass('disabled');
    	    $("#deactivate_user_account_confirm").removeAttr("href"); 
    	    
    	}
    });
    
    $('#ChangeOfHeart').click(function(){
    	
    	$("#DeactivateForm").hide();
    	$('a[name="deactivate_user_account"]').show();
        $("#deactivate_user_account_confirm").addClass('disabled');
    	$("#deactivate_user_account_confirm").removeAttr("href"); 
    	    
    	
    });
   
});

$(document).ready(function(){
    
    $('label[for="facebook_connect"]').click(function(){
    	if($(this).children('#facebook_connect').is(':checked')){
    	    $(this).children('.switch').children(':first').attr({"class":"shadow"});
    	    $(this).children('.switch').children('.border').children('.knob').css('margin-left','0%');
    	    $(this).children('#facebook_connect').prop("checked", false);
    	}else{
    		$(this).children('.switch').children(':first').attr({"class":"shadow on"});
    	    $(this).children('.switch').children('.border').children('.knob').css('margin-left','62%');
    	    $(this).children('#facebook_connect').checked = true;
    	    $(this).children('#facebook_connect').prop("checked", true);
    	}
    });
    
    $('label[for="facebook_timeline"]').click(function(){
    	if($(this).children('#facebook_timeline').is(':checked')){
    	    $(this).children('.switch').children(':first').attr({"class":"shadow"});
    	    $(this).children('.switch').children('.border').children('.knob').css('margin-left','0%');
    	    $(this).children('#facebook_timeline').prop("checked", false);
    	}else{
    		$(this).children('.switch').children(':first').attr({"class":"shadow on"});
    	    $(this).children('.switch').children('.border').children('.knob').css('margin-left','62%');
    	    $(this).children('#facebook_timeline').checked = true;
    	    $(this).children('#facebook_timeline').prop("checked", true);
    	}
    });
    
    $('label[for="twitter_connect"]').click(function(){
    	if($(this).children('#twitter_connect').is(':checked')){
    	    $(this).children('.switch').children(':first').attr({"class":"shadow"});
    	    $(this).children('.switch').children('.border').children('.knob').css('margin-left','0%');
    	    $(this).children('#twitter_connect').prop("checked", false);
    	}else{
    		$(this).children('.switch').children(':first').attr({"class":"shadow on"});
    	    $(this).children('.switch').children('.border').children('.knob').css('margin-left','62%');
    	    $(this).children('#twitter_connect').checked = true;
    	    $(this).children('#twitter_connect').prop("checked", true);
    	}
    });
});

    
    


