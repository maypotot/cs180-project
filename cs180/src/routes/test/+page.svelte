<script>
  let imageFile;
  let imagePreview = null;

  function handleFileChange(event) {
    const file = event.target.files[0];
    if (file && file.type.startsWith("image/")) {
      imageFile = file;
      const reader = new FileReader();
      reader.onload = (e) => {
        imagePreview = e.target.result;
      };
      reader.readAsDataURL(file);
    } else {
      imagePreview = null;
    }
  }
</script>
<div class="flex justify-center p-12 space-y-4 max-w-10xl">
    <div class="flex-col w-10/12 max-w-5xl text-center bg-gray-100 rounded-lg shadow-lg p-8">
        <h1 class="text-7xl font-bold mb-12">Test</h1>

        <div class="flex flex-col items-center gap-4 p-4 rounded-xl w-full max-w-md mx-auto shadow">

            
        <form action="/predict" method="post" enctype="multipart/form-data">
            <label for="fileInput" class="choose_image">Choose image</label>
            <input
                type="file"
                accept="image/*,.zip"
                on:change={handleFileChange}
                class="font-mono block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4
                    file:rounded-full file:border-0 file:text-sm file:font-semibold
                    file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
            <input type="submit" value="Upload" class="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-6 rounded-md transition-colors duration-200">
        </form>

        {#if imagePreview}
            <img src={imagePreview} alt="Preview" class="mt-4 rounded-lg shadow max-h-64 object-contain" />
        {/if}
        </div>
    </div>
</div>
