import re

with open("frontend/src/pages/admin/components/AddUnitModal.jsx", "r") as f:
    content = f.read()

# 1. Remove grid and photo col
content = content.replace('<div className="grid grid-cols-1 lg:grid-cols-12 gap-8">', '<div className="max-w-4xl mx-auto">')

# We need to remove the Photo Col and the Form Fields Col wrapper
photo_col = """            {/* Photo Col */}
            <div className="lg:col-span-3 flex flex-col items-center">
              <div 
                onClick={() => fileInputRef.current?.click()}
                className={`w-full aspect-video rounded-xl border-2 border-dashed flex flex-col items-center justify-center cursor-pointer transition-colors group mb-3 relative overflow-hidden ${photoPreview ? 'border-slate-200 bg-white' : 'border-slate-300 bg-white text-slate-400 hover:bg-slate-50 hover:border-blue-400 hover:text-blue-500'}`}
              >
                {photoPreview ? (
                  <img src={photoPreview} alt="Preview" className="w-full h-full object-cover" />
                ) : (
                  <>
                    <Upload className="w-8 h-8 mb-2 group-hover:scale-110 transition-transform" />
                    <span className="text-xs font-medium">Upload Photo</span>
                  </>
                )}
              </div>
              <input type="file" ref={fileInputRef} onChange={handlePhotoUpload} accept="image/*" className="hidden" />
              {photoPreview ? (
                <button type="button" onClick={() => setPhotoPreview(null)} className="text-[11px] text-red-600 font-medium w-full text-center hover:underline">Remove Photo</button>
              ) : (
                <p className="text-[10px] text-center text-slate-500">JPG or PNG, max 5MB (16:9 ratio)</p>
              )}
            </div>

            {/* Form Fields Col */}
            <div className="lg:col-span-9 space-y-8">"""

content = content.replace(photo_col, '<div className="space-y-8">')

# Make sure we don't have an extra closing div. We replaced 2 divs opening with 1. 
# We need to remove one closing div at the end of Modal Body.
modal_body_end = """              </section>

            </div>
          </div>
        </div>"""

content = content.replace(modal_body_end, """              </section>

          </div>
        </div>""")


# 2. Inject photo upload into Section 1
section_1_start = """              {/* Section 1: Vehicle Info */}
              <section>
                <h3 className="text-sm font-bold text-slate-900 mb-4 uppercase tracking-wider pb-2 border-b border-slate-200">Vehicle Information</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">"""

section_1_new = """              {/* Section 1: Vehicle Info */}
              <section>
                <h3 className="text-sm font-bold text-slate-900 mb-4 uppercase tracking-wider pb-2 border-b border-slate-200">Vehicle Information</h3>
                
                <div className="flex flex-col md:flex-row gap-6">
                  {/* Photo Upload */}
                  <div className="w-full md:w-64 shrink-0 flex flex-col items-center">
                    <label className="block text-xs font-semibold text-slate-700 mb-2 self-start">Unit Photo</label>
                    <div 
                      onClick={() => fileInputRef.current?.click()}
                      className={`w-full aspect-video rounded-xl border-2 border-dashed flex flex-col items-center justify-center cursor-pointer transition-colors group mb-2 relative overflow-hidden ${photoPreview ? 'border-slate-200 bg-white' : 'border-slate-300 bg-slate-50 text-slate-400 hover:bg-slate-100 hover:border-blue-400 hover:text-blue-500'}`}
                    >
                      {photoPreview ? (
                        <img src={photoPreview} alt="Preview" className="w-full h-full object-cover" />
                      ) : (
                        <>
                          <Upload className="w-6 h-6 mb-2 group-hover:scale-110 transition-transform" />
                          <span className="text-xs font-medium">Upload</span>
                        </>
                      )}
                    </div>
                    <input type="file" ref={fileInputRef} onChange={handlePhotoUpload} accept="image/*" className="hidden" />
                    {photoPreview ? (
                      <button type="button" onClick={() => setPhotoPreview(null)} className="text-[11px] text-red-600 font-medium w-full text-center hover:underline">Remove Photo</button>
                    ) : (
                      <p className="text-[10px] text-center text-slate-500">JPG or PNG (16:9)</p>
                    )}
                  </div>

                  <div className="flex-1 grid grid-cols-1 sm:grid-cols-2 gap-4">"""

content = content.replace(section_1_start, section_1_new)

# We need to close the flex container after section 1.
section_1_end = """                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4 pt-4 border-t border-slate-200">"""

section_1_end_new = """                  </div>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4 pt-4 border-t border-slate-200">"""

content = content.replace(section_1_end, section_1_end_new)

with open("frontend/src/pages/admin/components/AddUnitModal.jsx", "w") as f:
    f.write(content)
