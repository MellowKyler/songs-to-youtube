class Constant:
    """A class for storing constants for YoutubeUploader class"""
    YOUTUBE_URL = 'https://www.youtube.com'
    YOUTUBE_STUDIO_URL = 'https://studio.youtube.com'
    YOUTUBE_UPLOAD_URL = 'https://www.youtube.com/upload'
    USER_WAITING_TIME = 1
    USER_AVATAR_XPATH = '//img[@id="img"][@alt="Avatar image"]'
    VIDEO_TITLE = 'title'
    VIDEO_DESCRIPTION = 'description'
    PLAYLIST = 'playlist'
    TAGS = 'tags'
    DESCRIPTION_CONTAINER = '//*[@label="Description"]'
    MORE_OPTIONS_CONTAINER = '//*[text() = "More options"]'
    PLAYLIST_CONTAINER = '//*[@label="Playlists"]'
    PLAYLIST_SEARCH = '//*[@id="search-input"]'
    PLAYLIST_SEARCH_CLEAR_BUTTON = '//*[@class="style-scope ytcp-playlist-dialog"]/iron-icon[@class="remove-defaults style-scope ytcp-icon-button"]'
    PLAYLIST_NEW_BUTTON = '//*[text() = "New playlist"]'
    PLAYLIST_NEW_TITLE = '//div[@id="create-playlist-form"]/div/ytcp-form-textarea/div/textarea'
    PLAYLIST_DONE_BUTTON = '//*[@class="done-button action-button style-scope ytcp-playlist-dialog"]/*[text() = "Done"]'
    PLAYLIST_CREATE_BUTTON = '//*[@class="create-playlist-button action-button style-scope ytcp-playlist-dialog"][@label="Create"]'
    PLAYLIST_VISIBILITY_DROPDOWN = '//*[@class="input-container visibility style-scope ytcp-playlist-dialog"]'
    PLAYLIST_LABEL = "//label[./span/span[@class='label label-text style-scope ytcp-checkbox-group']]"
    TOOLTIP = '//ytcp-paper-tooltip'
    TAGS_TEXT_INPUT = '//input[@aria-label="Tags"]'
    TEXTBOX = 'textbox'
    TEXT_INPUT = 'text-input'
    RADIO_LABEL = 'radioLabel'
    STATUS_CONTAINER = '//*[@class="progress-label style-scope ytcp-video-upload-progress"]'
    NOT_MADE_FOR_KIDS_LABEL = 'NOT_MADE_FOR_KIDS'
    NEXT_BUTTON = 'next-button'
    VIDEO_URL_CONTAINER = "//span[@class='video-url-fadeable style-scope ytcp-video-info']"
    VIDEO_URL_ELEMENT = "//a[@class='style-scope ytcp-video-info']"
    HREF = 'href'
    UPLOADED = 'Uploading'
    ERROR_CONTAINER = '//*[@id="error-message"]'
    VIDEO_NOT_FOUND_ERROR = 'Could not find video_id'
    DONE_BUTTON = 'done-button'
    INPUT_FILE_VIDEO = "//input[@type='file']"
    USERNAME_ID = "account-name"
    VIDEO_PUBLISHED_DIALOG = '//*[@id="dialog-title"]'

    MAX_TITLE_LENGTH = 100
    MAX_DESCRIPTION_LENGTH = 5000
    MAX_TAGS_LENGTH = 500
