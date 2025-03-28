MESSAGES = {
    'en': {
        'folder_path_prompt': "Please enter the folder path containing txt files (default: {}): ",
        'delete_confirm': "Delete original txt files? (y/n, default: n): ",
        'invalid_input': "Invalid input, please enter y or n",
        'error_folder': "Error: The folder {} does not exist or is not a directory",
        'warning_no_files': "Warning: No txt files found in {}",
        'found_files': "Found {} txt files",
        'processing': "Processing: {}",
        'saved': "Saved: {}",
        'deleted_original': "Deleted original file: {}",
        'conversion_failed': "Conversion failed: {}",
        'api_error': "API call error: {}",
        'waiting_retry': "Waiting {} seconds before retry... (attempt {}/{})",
        'max_retries': "Maximum retry attempts ({}) reached, conversion failed.",
        'language_select': "Select language/选择语言: [1] English [2] 中文 (default: 1): "
    },
    'zh': {
        'folder_path_prompt': "请输入要转换的文件夹路径 (默认: {}): ",
        'delete_confirm': "是否删除原始txt文件? (y/n, 默认: n): ",
        'invalid_input': "无效输入，请输入 y 或 n",
        'error_folder': "错误: 文件夹 {} 不存在或不是一个目录",
        'warning_no_files': "警告: 在 {} 中没有找到txt文件",
        'found_files': "找到 {} 个txt文件",
        'processing': "处理: {}",
        'saved': "已保存: {}",
        'deleted_original': "已删除原始文件: {}",
        'conversion_failed': "转换失败: {}",
        'api_error': "API调用出错: {}",
        'waiting_retry': "等待 {} 秒后重试... (尝试 {}/{})",
        'max_retries': "已达到最大重试次数 ({})，转换失败。",
        'language_select': "Select language/选择语言: [1] English [2] 中文 (default: 1): "
    }
}

def get_message(lang, key, *args):
    """获取指定语言的消息，并进行格式化"""
    if lang not in MESSAGES or key not in MESSAGES[lang]:
        # 如果找不到指定语言或消息键，则使用英文默认值
        return MESSAGES['en'].get(key, key).format(*args)
    return MESSAGES[lang][key].format(*args)
