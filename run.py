import view
import model

def run():
    pref = view.pref()
    if pref==0:
        return view.saybye()
    else:
        view.answer(model.selection(pref))
        return run()

run()
