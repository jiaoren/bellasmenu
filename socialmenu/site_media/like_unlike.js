$(document).ready(function () {
    $(".actions a").click(function clicked(){
  	    ele = $(this)
  	    which = jQuery.trim($(this).text());
  	    if(which == 'Like'){
  	    	menuid = jQuery.trim($(this).attr('data-id'));
  	    	$.get("/ajax_like?q="+menuid,function(data){
  	    		if(jQuery.trim(data)=='true'){
  	    			ele.text("Unlike");
  	    		}
  	    		
  	    	});
  	    }else if(which == 'Unlike'){
  	    	menuid = jQuery.trim($(this).attr('data-id'));
  	    	$.get("/ajax_unlike?q="+menuid,function(data){
  	    		if(jQuery.trim(data)=='true'){
  	    			
  	    			ele.text("Like");
  	    			ele.prepend('<em></em>');
  	    		}
  	    		
  	    	});
  	    	
  	    }
  	    
    });
});

