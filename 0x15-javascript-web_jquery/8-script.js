$.get("https://swapi-api.hbtn.io/api/films/?format=json",
 function(data, status){
 	const result = data.results;
 	const titles = [];
 	for (val of result) {
 		$("UL#list_movies").append(`<li>${val.title}</li>`);
 	}
});
