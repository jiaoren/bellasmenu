$(document).ready(function () {
    $(".Button.Button13.RedButton.followuserbutton").click(function clicked(){
  	    
  	    ele = $(this)
  	    which = jQuery.trim($(this).text());
  	    if(which == 'Follow All'){
  	    	
  	    	$.get("/follow/"+$(this).attr('action'),function(data){
  	    		if(jQuery.trim(data)=='true'){
  	    			ele.text("Unfollow All");
  	    		}
  	    		
  	    	});
  	    }else if(which == 'Unfollow All'){
  	    	
  	    	$.get("/unfollow/"+$(this).attr('action'),function(data){
  	    		if(jQuery.trim(data)=='true'){
  	    			
  	    			ele.text("Follow All");
  	    			
  	    		}
  	    		
  	    	});
  	    	
  	    }
  	    
    });
    
});

