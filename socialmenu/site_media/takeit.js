$(document).ready(function(){
	$("a.close").click(function(){
	   $('#Repin').remove();
	
	});
	
	$('.BoardSelector.BoardPicker').click(function(){
	    $(this).children('.BoardList').show();
    });
    
    
    $(".BoardList ul li").click(function(){
    	$('.CurrentBoard').text($(this).text());
    	$('.BoardList').hide();
    	return false;
    });
    
   
   $("button").click(function(){
    	$("form #takeit_catagory").val($('.CurrentBoard').text());
    	$("form #details").val($('.DescriptionTextarea').val());
    	$('#repinform').submit();
    });
    
});


function bindTakeItHandler() {
	
    $('#repinform').submit(function() {
    	
        $.ajax({
            type: "GET",
            data: $(this).serialize(),
            url: '/posttakeit/',
            cache: false,
            dataType: "html",
            success: function(data) {          
	           $('.modal.wide.PostSuccess').css('display','block');
	           $('.modal.wide.PostSuccess').css('bottom','50%');
	           $('.modal.wide.PostSetup').css('bottom','125%');
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
               
            }
        });
        return false;
    });
}
 

$(document).ready(function() {
    bindTakeItHandler();
});