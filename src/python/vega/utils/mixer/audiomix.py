import wave

from mixer import Mixer


class AudioMix(Mixer):
    def _mix(self, instru, vocal, out):
        with wave.open(instru, "rb") as file1:
            with wave.open(vocal, "rb") as file2:
                params1 = file1.getparams()
                params2 = file2.getparams()
                start_time = 5
                start_frame = int(start_time * params2.framerate)
                output_params = params1._replace(nframes=params1.nframes + params2.nframes - start_frame)
                with wave.open(out, "wb") as output_file:
                    output_file.setparams(output_params)
                    output_file.writeframes(file1.readframes(file1.getnframes()))
                    file2.setpos(start_frame)
                    output_file.writeframes(file2.readframes(file2.getnframes()))


if __name__ == "__main__":
    a = AudioMix("/home/Temp/1-sept-2023")
    a._mix(
            "/home/Downloads/Untitled1.wav",
            "/home/Downloads/Untitled.wav",
            a._generate_filepath())
    print(a)