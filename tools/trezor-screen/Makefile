all: trezor-screen-pin.png

trezor-screen-%.png: %.txt
	./trezor-screen.py $<

clean:
	rm -f trezor-screen-*.png
