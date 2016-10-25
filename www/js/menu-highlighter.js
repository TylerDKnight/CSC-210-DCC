// highlights the menu item anchor that has the id passed to the function
function highlightMenuItemFromId(id_no_hashtag) {
	$(function() {
		$('#' + id_no_hashtag).css('color', '#00cccc');
	});
}
