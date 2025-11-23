from IPython.display import HTML, display


def form_maker(form_id):
#     <input name="Answer" type="text" placeholder="Answer" required>
    myfunc2="""
<form name="submit-to-google-sheet">
  <textarea id="Answer" name="Answer" rows="4" cols="50">Your answer here</textarea>
  <input name="Quest" type="hidden" value="%s" required>
  <button type="submit">Send</button>
</form>

<script>
  const scriptURL = 'https://script.google.com/macros/s/AKfycbw3napF29Lqt4BLM-l0xtZv0aAfikLMuXTc1KeSPh_cFY5O71jYdcGnaayMPz83NnNjsA/exec'
  const form = document.forms['submit-to-google-sheet']

  form.addEventListener('submit', e => {
    e.preventDefault()
    fetch(scriptURL, { method: 'POST', body: new FormData(form)})
  })
</script>
""" % form_id

    display(HTML(myfunc2))
    