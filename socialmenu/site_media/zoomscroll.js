$(document).ready(function(){
	$("#CloseupComment").focus(function(){
	    $(this).parent().siblings("#PinAddCommentControls").show();
	
	});
});

function bindPostCommentHandler() {
	
    $('form').submit(function() {
    	commetslistform = $(".PinComments");
        $.ajax({
            type: "POST",
            data: $(this).serialize(),
            url: $(this).attr('action'),
            cache: false,
            dataType: "html",
            success: function(data) {          
	           commentid = $(data).attr('comment-id');
	           var newdata = $(data).attr('class','comment');
	           var deletecomment = "<a data=\""+commentid+"\" href=\"/pin/"+commentid+"/deletecomment/\" title=\"Remove Comment\" class=\"DeleteComment floatRight tipsyHover\">X</a>";
	           
	           newdata.children('a').attr('class','CommenterImage');
	           newdata.prepend(deletecomment);
	           newdata.children('p').attr('class','CommenterMeta');
               commetslistform.append(newdata);
	           
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
               
            }
        });
        return false;
    });
}
 

$(document).ready(function() {
    bindPostCommentHandler();
});


$(document).ready(function() {
    $('textarea').keyup(function() {

        var empty = false;
        
        if ($(this).val().length == 0) {
            empty = true;
        }

        if (empty) {
            $('#PostComment').attr('disabled', 'true');
        } else {
        	$('#PostComment').removeAttr('disabled');
            $('#PostComment').removeClass('disabled');
        }
    });
});