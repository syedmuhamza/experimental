import streamlit as st
from read_write import read_file, write_file, update_file

st.set_page_config('HOME', layout='wide')
st.title(':blue[BUY LIST]')
tabs = st.tabs([':green[**Grocery**]'])
grocery_new_item = tabs[0].text_input(':blue[**Add New Item**]')
button_grocery_new_item = tabs[0].button('ADD')
grocery_pending, grocery_completed = tabs[0].columns(2)
container_grocery_pending = grocery_pending.container(border=True)
container_grocery_completed = grocery_completed.container(border=True)
container_grocery_pending.markdown(':red[**Pending**]')
container_grocery_completed.markdown(':green[**Completed**]')
grocery_items = read_file('grocery.txt')

if button_grocery_new_item:
    current = read_file('grocery.txt')
    duplicate = False
    for item in current:
        if item.strip('\n') == grocery_new_item:
            st.info(f'{item} already exist in Pending')
            duplicate = True
    if duplicate is False:
        write_file('grocery.txt', grocery_new_item)
        grocery_items = read_file('grocery.txt')

grocery_checkboxes = []
for index, item in enumerate(grocery_items):
    try:
        is_checked = container_grocery_pending.checkbox(item, key=item)
        grocery_checkboxes.append((item, is_checked))
    except:
        st.info('Cannot add two items with the same name')
for item, is_checked in grocery_checkboxes:
    if is_checked:
        print('before', grocery_items)
        grocery_items.remove(item)
        print('after', grocery_items)
        update_file('grocery.txt', grocery_items)
        write_file('grocery_completed.txt', item.strip('\n'))
        # grocery_items.clear()
        st.success(f'{item} has been marked as Completed')


with container_grocery_completed:
    completed_grocery = read_file('grocery_completed.txt')
    for index, item in enumerate(completed_grocery):
        container_grocery_completed.markdown(f'{index+1} - {item}')
    clear_button = container_grocery_completed.button('CLEAR')
    if clear_button:
        update_file('grocery_completed.txt', [])





