
	
   
	//======= User Edit =======//
	function fn_userEdit(id){
		$("#hidden_div").load("./ajax/userEdit.php", {id: id}, function(){
			$.blockUI({
				message: $('#hidden_div'),
				css:{
					top: '20%'
				}
			}); 
		});
	};



