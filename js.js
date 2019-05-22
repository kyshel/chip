	
  // jquery-3.3.1.min.js
  
  
  
  
  function ajax_req1(url,http_method = 'GET',data = undefined,contentType = undefined){
		before_ajax()
		$.ajax({
			method: http_method,
			url: url ,
			data: data,

			contentType: contentType,
		// async: async,
		// dataType:'json',
		// contentType: 'application/json;charset=UTF-8',
	}).done( function(response,status,xhr) {
		ajax_res(url, response)
		after_ajax(url,response)
	}).fail( function(xhr,status,e) {
		after_ajax(url,xhr)
		console.log('Ajax Fail>>>')
		console.log(e)
		console.log('Ajax Fail<<<')
	});
}
