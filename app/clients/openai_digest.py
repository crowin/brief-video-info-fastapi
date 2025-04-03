import openai


class OpenAIClient:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_text_summary(self, subtitles: str, language: str, ratio: float = 0.2) -> str:
        prompt_ru = f"Сделай краткий пересказ для следующего текста. Постарайтесь оставить основные моменты и важные детали. Также учитывайте коэффициент длины пересказа ({ratio}):\n\n{subtitles}"
        prompt_en = f"Provide a brief summary of the following text. Try to retain the key points and important details. Also, take into account the summary length ratio ({ratio}):\n\n{subtitles}"
        prompt = prompt_ru if language == "ru" else prompt_en

        estimate_duration = self.estimate_video_duration(subtitles)
        summary_duration = self.generate_summary_duration(estimate_duration, ratio)

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=summary_duration,
            temperature=0.7
        )

        return response.choices[0].text.strip()

    @staticmethod
    def estimate_video_duration(subtitles_text: str, avg_word_length: int = 5, words_per_minute: int = 150) -> float:
        """
        Оцениваем длительность видео по тексту субтитров.

        :param subtitles_text: Текст субтитров.
        :param avg_word_length: Среднее количество символов в слове.
        :param words_per_minute: Среднее количество слов, произносимых в минуту.
        :return: Ожидаемая длительность видео в минутах.
        """
        # Подсчитываем количество символов в субтитрах
        num_characters = len(subtitles_text)

        # Приблизительное количество слов в субтитрах
        num_words = num_characters / avg_word_length

        # Рассчитываем время (в минутах), которое займет чтение этих слов с учетом средней скорости речи
        video_duration_minutes = num_words / words_per_minute

        return video_duration_minutes

    @staticmethod
    def generate_summary_duration(video_duration_minutes: float, summary_ratio: float = 0.2) -> float:
        """
        Генерируем длительность пересказа на основе коэффициента.

        :param video_duration_minutes: Длительность видео в минутах.
        :param summary_ratio: Коэффициент длины пересказа.
        :return: Ожидаемая длительность пересказа в минутах.
        """
        return video_duration_minutes * summary_ratio