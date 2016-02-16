$(document).ready(function(){
	$('.colorless.noDescription').click(function(){
		$('.colorless.noDescription').css('display','none');
		$('#editDescription').css('display','block');
		$('#editDescription textarea').val('');
	});
	
	$('textarea').keyup(function() {
        var empty = false;
        if ($(this).val().length == 0) {
            empty = true;
        }
        if (empty) {
            $('#submitedit').attr('disabled', 'true');
            $('#submitedit').addClass('disabled', 'true');
        } else {
        	$('#submitedit').removeAttr('disabled');
            $('#submitedit').removeClass('disabled');
        }
    });
    
    $('#submitedit').click(function() {  
    	var description = $('#editDescription textarea').val();
        $.ajax({
            type: "GET",
            data: {'description':description},
            url: '/ajax_edit_about/',
            cache: false,
            dataType: "html",
            success: function(data) {          
	           if(data == 'true'){
	           	   
	           	   $('.content h1').after('<p class="colormuted">'+description+'</p>');
	               $('.colorless.noDescription').css('display','none');
		           $('#editDescription').css('display','none');
		          
	           }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
               
            }
        });
        return false;
    });
});
