import hashlib
import wave
import time
import json

class SonicAnalysisService:
    def __init__(self, timeout=5):
        self.cache = {}
        self.timeout = timeout

    def analyze(self, file_path):
        file_hash = self._hash_file(file_path)

        # Check if the result is cached
        if file_hash in self.cache:
            cached_result, timestamp = self.cache[file_hash]
            if time.time() - timestamp < self.timeout:
                return cached_result

        # Analyze the WAV file
        result = self._perform_analysis(file_path)
        self.cache[file_hash] = (result, time.time())
        return result

    def _hash_file(self, file_path):
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            hasher.update(f.read())
        return hasher.hexdigest()

    def _perform_analysis(self, file_path):
        with wave.open(file_path, 'rb') as wav_file:
            channels = wav_file.getnchannels()
            sample_rate = wav_file.getframerate()
            frame_count = wav_file.getnframes()
            duration = frame_count / sample_rate

            result = {
                "version": "2026-04-17",
                "channels": channels,
                "sample_rate": sample_rate,
                "duration": duration
            }
            return result
