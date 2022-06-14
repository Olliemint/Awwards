$(document).ready(function(){
    $("#work4").hover(function(){
        $(this).fadeTo("slow",0.6)
        $("#overlay").show();},
        function(){
            $(this).fadeTo("slow", 1)
            $("#overlay").hide();
    });

  });


  console.log("hello")