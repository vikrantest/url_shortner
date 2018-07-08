const prefixUrl = 'http://localhost:8000'


//modularize below code
$(document).ready(
	function(){
		console.log(window.location.pathname);
		// $.getJSON('../config/message.json',function(data){
		// 	console.log(data);
		// });
		const message_handler = {'Invalid Request':'Something went wrong , please try after sometime.','Invalid Url':'Invalid URL for shortening.'};
		$('#main_url').on('paste', function() {
		    setTimeout(function () { 
		        hideError('#shurl_result_error','input_box_error','#main_url')
				processSHurlRequest();
		    }, 100);
		});
		$('#generate_shurl').click(function(){
			hideError('#shurl_result_error','input_box_error','#main_url')
			processSHurlRequest();
			
		});

		function handleShurlRequestData(selector){
			const big_url = $(selector).val();
			let new_shurl = false;
			if(big_url.length>0){
				if($('#new_shurl_flag').is(":checked")){
					new_shurl = true;
				}
				return {'shurl_url':big_url,'new_shurl':new_shurl};
			}
			else{
				return null;
			}
		}

		function processSHurlRequest(){
			this.url = 'http://localhost:8000/myshurl/generate-shurl/';
			let request_data = handleShurlRequestData('#main_url');
			console.log(request_data);
			if(request_data){
				if(!validateUrl(request_data.shurl_url)){
					displayError('#shurl_result_error',message_handler['Invalid Url'],'input_box_error','#main_url')
				}
				else{
					getShurl(request_data,'POST');
				}
			}
		}

		function getShurl(param,method){
			$.ajax({
				url:'http://localhost:8000/myshurl/generate-shurl/',
				method:method,
				data: param,
				success: function(result){
					const shurl = `${prefixUrl}/${result.shurl_slug}`
					$('#shurl_result').text(shurl);
				},
				error: function(error){
					const error_message= error.responseJSON.error;
					displayError('#shurl_result_error',message_handler[error_message])
				}

			})
		}

		function validateUrl(url){
			const reg = /^(http[s]?:\/\/){0,1}(www\.){0,1}[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,5}[\.]{0,1}/
			console.log(url);
			return reg.test(url);
		}

		function displayError(selector,text,error_class=null,error_class_selector=null){
			$(selector).show();
			$(selector).text(text);
			$(error_class_selector).addClass(error_class);
		}
		function hideError(selector,error_class=null,error_class_selector=null){
			$(selector).hide();
			$(error_class_selector).removeClass(error_class)
		}

});

