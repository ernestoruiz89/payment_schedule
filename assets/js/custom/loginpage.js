$(function() {

	//===== Placeholder =====//
	
	$('input[placeholder], textarea[placeholder]').placeholder();


	
	
	//===== Dual select boxes =====//
	
	$.configureBoxes();
	

	
	//===== Validation engine =====//
	
	$("#validate").validationEngine();


/* Other plugins
================================================== */

/* UI stuff
================================================== */


	//===== Form elements styling =====//
	
	$("select, input:checkbox, input:radio, input:file").uniform();

	
});