RUN := jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=1800 --output-dir $(or $(TMPDIR),/tmp)/cfdc-test

.PHONY: refs student test check clean

refs:  ## render [@key] citations from references.bib into instructor/
	python render_refs.py

student: refs  ## regenerate student/ from instructor/
	python make_student.py

test: student  ## execute every instructor and student notebook (outputs go to a temp dir)
	$(RUN) instructor/*.ipynb student/*.ipynb

check:  ## what CI checks besides execution: refs rendered, student/ in sync, no outputs committed
	python render_refs.py --check
	python make_student.py > /dev/null && git diff --exit-code -- student/
	python -c "import glob, nbformat, sys; bad = [f for f in glob.glob('*/*.ipynb') if any(c.get('outputs') for c in nbformat.read(f, 4).cells)]; sys.exit(f'outputs not cleared: {bad}' if bad else 0)"

clean:  ## clear all outputs in place (run before committing)
	jupyter nbconvert --clear-output --inplace instructor/*.ipynb student/*.ipynb
