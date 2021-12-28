// Add search 
//* Enqueue scripts and styles
add_action( 'wp_enqueue_scripts', 'custom_enqueue_scripts_styles' );
function custom_enqueue_scripts_styles() {
    wp_enqueue_script( 'global', get_bloginfo( 'stylesheet_directory' ) . '/js/global.js', array( 'jquery' ), '1.0.0', true );
 
}
 
add_filter( 'wp_nav_menu_items', 'theme_menu_extras', 10, 2 );
/**
 * Filter menu items to append a search form.
 *
 * @param string   $menu HTML string of list items.
 * @param stdClass $args Menu arguments.
 *
 * @return string Amended HTML string of list items.
 */
function theme_menu_extras( $menu, $args ) {
 
    if ( 'primary' !== $args->theme_location )
        return $menu;
 
    $menu .= '<li class="search"><a id="main-nav-search-link" class="icon-search"></a><div class="search-div">' . get_search_form( false ) . '</div></li>';
    
    return $menu;
 
}
 
//* Customize search form input button text
add_filter( 'genesis_search_button_text', 'sp_search_button_text' );
function sp_search_button_text( $text ) {
    return esc_attr( 'Ok' );
}