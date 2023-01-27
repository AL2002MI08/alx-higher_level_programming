$('document').ready(() => {
  $('DIV#add_item').on('click', () => {
    $('UL.my_list').append($('<li></li>').text('Item'));
  });
  $('DIV#remove_item').on('click', () => {
    $('UL.my_list li:last').remove();
  });
  $('DIV#clear_list').on('click', () => {
    $('UL.my_list').empty();
  });
});
