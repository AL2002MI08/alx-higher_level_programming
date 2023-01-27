$('DIV#add_item').on('click', () => {
  const item = $('<li></li>').text('Item');
  $('UL.my_list').append(item);
});
