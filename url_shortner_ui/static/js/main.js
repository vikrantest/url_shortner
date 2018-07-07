
const prefixUrl = 'http://localhost:8000'

$(document).ready(
	function(){
		$('#generate_shurl').click(function(){
			this.url = 'http://localhost:8000/myshurl/generate-shurl/';
			alert($('#main_url').val());
			getShurl();
		});

		function getShurl(){
			const shurl = $('#main_url').val();
			param = {'shurl_url':shurl}
			$.ajax({
				url:'http://localhost:8000/myshurl/generate-shurl/',
				method:'POST',
				data: param,
				success: function(result){
					console.log('success==================',result);
					const shurl = `${prefixUrl}/${result.shurl_slug}`
					$('#shurl_result').text(shurl);
				},
				error: function(error){
					console.log('error+++++++++++++++',error);
				}

			})
		}

});

