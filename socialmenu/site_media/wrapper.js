$(document).ready(function(){
	$("div #commentpin").click(function(){
		if($(this).parent().parent().siblings("div #commentarea").css("display") == "none"){
		    $(this).parent().parent().siblings("div #commentarea").show();
		    $('#ColumnContainer').masonry( 'reload' );
		}else{
			$(this).parent().parent().siblings("div #commentarea").hide();
			$('#ColumnContainer').masonry( 'reload' );
		}
	});
});

$(document).ready(function(){
	$("textarea").focus(function(){
	    $(this).siblings("button").css({"visibility":"visible","display":"inline"});
	    $('#ColumnContainer').masonry( 'reload' );
	
	});
});

$(document).ready(function(){
	$(".PinImage.ImgLink").click(function(){
		
	    $.ajax({
            type: "GET",
            data: {'menuid':$(this).attr('data-menu-id')},
            url: '/zoomscroll/',
            cache: false,
            dataType: "html",
            success: function(html, textStatus) {
            	$('#ColumnContainer').append(html);
                $('html').click(function() {
                    $('#zoomScroll').remove();
                });

                $('#zoom').click(function(event){
                    event.stopPropagation();
                });
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
               alert("failed");
            }
        });
	    
	    return false;
	});
	
	
	
});

$(document).ready(function(){
	$(".Button.Button11.WhiteButton.ContrastButton.repin_link").click(function(){
		$.ajax({
            type: "GET",
            data: {'menuid':$(this).attr('data-id')},
            url: $(this).attr('href'),
            cache: false,
            dataType: "html",
            success: function(html, textStatus) {
            	$("#wrapper").before(html);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
               
            }
        });
		return false;
	});
	
	
	
});
	
function bindPostCommentHandler() {
	
    $('form').submit(function() {
    	who = $(this).children(".usercommented").val();
    	commetslistform = $(this).parent().siblings('.comments.colormuted');
        $.ajax({
            type: "POST",
            data: $(this).serialize(),
            url: $(this).attr('action'),
            cache: false,
            dataType: "html",
            success: function(html, textStatus) {
            	if(commetslistform.children().last().get(0).tagName == "DIV"){
            		
            		commetslistform.append(html);
            	}else{
            		
            		commetslistform.children().last().before(html);
            	}
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

$(function(){
  $('#ColumnContainer').masonry({
    // options
    itemSelector : '.pin',
    columnWidth : 237,
    
  });
});


$(document).ready(function(){
// Hide the toTop button when the page loads.
       $('.endless_more').css('display','none');
 // This function runs every time the user scrolls the page.
        $(window).scroll(function(){
// Check weather the user has scrolled down (if "scrollTop()"" is more than 0)
            if($(window).scrollTop() > 0){
// If it's more than or equal to 0, show the toTop button.  
                $("#ScrollToTop").removeClass('Offscreen');
            }else {
 // If it's less than 0 (at the top), hide the toTop button.
                $("#ScrollToTop").addClass('Offscreen');
            }
        });
 
// When the user clicks the toTop button, we want the page to scroll to the top.
    $("#ScrollToTop").click(function(){

// Animate the scrolling motion.
        $("html, body").animate({
            scrollTop:0
         },"slow");
         $("#ScrollToTop").addClass('Offscreen');
    });
});