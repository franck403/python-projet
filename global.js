jQuery(function( $ ){
 
    $('#main-nav-search-link').click(function(){
        $('.search-div').show('slow');
    });
 
    $("*", document.body).click(function(event){
        // event.stopPropagation();
        var el = $(event.target);
        var gsfrm = $(el).closest('form');
        if(el.attr('id') !='main-nav-search-link' && el.attr('role') != 'search' && gsfrm.attr('role') != 'search'){
            $('.search-div').hide('slow');
        }
    });
 
});
function sitealert() {

    alert("a cause de code non sécuritaire du html voudevez allez sur mon autre site qui est https://sites.google.com/view/virusvirus04/accueil ");
  }
