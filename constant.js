const NAME_PLACEHOLDER = 'NAME_OF_PERSON';

const LAST_MESSAGE = '(//div[contains(@class, "message-out")])[last()]';
const MSG_TICK = '//span[contains(@data-icon, "check")]';

const XPATH = {
    CHAT : `//*[@title='${NAME_PLACEHOLDER}']/../../../../../..`,
    SIDE_PANEL : '//div[@id="pane-side"]',
    MESSAGEBOX : "//div[text()='Type a message']/following-sibling::div[@contenteditable='true']",
    ATTACHMENT_MENU : '//span[@data-icon="clip"]',
    GALLERY_BUTTON : '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]',
    IMAGE_CAPTION_INPUT : '//span[contains(text(), "Add a caption…")]/following-sibling::div//div[contains(@class, "copyable-text") and contains(@class, "selectable-text")]',
    NEW_CHAT_BUTTON : '//div[@title="New chat"]/../..',
    CONTACT_SEARCH_INPUT : '//*[text()="Search contacts"]/../label//*[@contenteditable="true"]',
    LAST_MESSAGE : LAST_MESSAGE,
    MSG_TICK : MSG_TICK,
    LAST_MESSAGE_DOUBLE_TICK : LAST_MESSAGE + MSG_TICK,
    QR_CODE: "//canvas[@aria-label='Scan me!']",
    USE_HERE_BUTTON: "//div[@role='button'][text()='Use Here']",

    // Error Handling Constants,
    LOADER_PROGRESS : "//progress[@dir='ltr']",
    RETRY_DIALOG_BOX : "//div[contains(text(), 'Trying to reach phone')]",
}

module.exports.XPATH = XPATH;
module.exports.NAME_PLACEHOLDER = NAME_PLACEHOLDER;
