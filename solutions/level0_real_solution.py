def clear_yard(pythin):
  for i in range(len(pythin.get_items())):
    pythin.eat(i)
    if pythin.is_full() == 3:
      pythin.swallow()
  if len(pythin.peek_stomach()) > 0:
    pythin.swallow()