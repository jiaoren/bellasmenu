$(document).ready(function () {
     $(".Button.Button13.WhiteButton.disabled.clickable.unfollowuserbutton").click(function clicked(){
     	
  	    ele = $(this)
  	    which = jQuery.trim($(this).text());
  	    if(which == 'Unfollow'){
  	    	
  	    	$.get("/unfollow/"+$(this).attr('action'),function(data){
  	    		if(jQuery.trim(data)=='true'){
  	    			ele.text("Follow");
                    ele.attr("class","Button Button13 WhiteButton clickable followuserbutton")
  	    		}
  	    		
  	    	});
  	    	
  	    }else{
  	    	
  	    	$.get("/follow/"+$(this).attr('action'),function(data){
  	    		if(jQuery.trim(data)=='true'){
  	    			ele.text("Unfollow");
  	    			ele.attr("class","Button Button13 WhiteButton disabled clickable unfollowuserbutton")
  	    		}
  	    		
  	    	});
  	    }
  	    
    });
    
    $(".Button.Button13.WhiteButton.clickable.followuserbutton").click(function clicked(){
     	
  	    ele = $(this)
  	    which = jQuery.trim($(this).text());
  	    if(which == 'Follow'){
  	    	
  	    	$.get("/follow/"+$(this).attr('action'),function(data){
  	    		if(jQuery.trim(data)=='true'){
  	    			ele.text("Unfollow");
  	    			ele.attr("class","Button Button13 WhiteButton disabled clickable unfollowuserbutton")
  	    		}
  	    		
  	    	});
  	    }else{
  	    	$.get("/unfollow/"+$(this).attr('action'),function(data){
  	    		if(jQuery.trim(data)=='true'){
  	    			ele.text("Follow");
                    ele.attr("class","Button Button13 WhiteButton clickable followuserbutton")
  	    		}
  	    		
  	    	});
  	    }
  	    
    });
});

