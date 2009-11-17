from google.appengine.api import images

def crop_and_resize_image_to_square(image_bytes, final_width, final_height, output_encoding=images.PNG):
    try:
        original_image = images.Image(image_bytes)
        original_width, original_height = original_image.width, original_image.height

        # Is the image square?
        if original_width != original_height:
            # No, so force it to be a square (cut off the long direction)
            if original_width < original_height:
                original_image.crop(0.0, 0.0, 1.0, float(original_width) / float(original_height))
            else:
                original_image.crop(0.0, 0.0, float(original_height) / float(original_width), 1.0)
        
        # Force the image to final desired size
        original_image.resize(width = final_width, height = final_height)

        # Get final bytes
        resized_bytes = original_image.execute_transforms(output_encoding)
    except images.Error:
        resized_bytes = None
        
    return resized_bytes
    