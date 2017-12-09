// $(document).ready(function() {
//     $('#submit').on('click', function(){

//         var query = $('#query').val()

//         $.ajax({
//             type: "POST",
//             url: "/getData",
//             // contentType: 'application/json; charset=UTF-8',
//             data: query,
//             // dataType: 'json',
//             // data: $('form').serialize(),
//             success: function(response){
//                 // $('#answer').html(response['key']);
//                 console.log(response['key'])
//             },
//             error: function(error){
//                 console.log(error);
//             },

//         });
//     });
// })


$( "#querySubmit" ).click(function( event ) {
  searchString = $("#query").val();
  var response =  $.ajax({
    url: "getInfo/?query=" + searchString,
    method: "POST",
    success: function(responsedata) {
     console.log(responsedata);
     $('#answer').text(responsedata['answer']);
     // $('#result > div > p').text(responsedata['answer']);
     // $('#result > a').attr('href', responsedata['link']);
    }
  });
  event.preventDefault();
});