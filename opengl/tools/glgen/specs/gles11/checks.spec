glClipPlanef check eqn 4
glClipPlanex check eqn 4
glGetClipPlanefOES check eqn 4
glGetClipPlanexOES check eqn 4
glDeleteBuffers check buffers n 
glDeleteTextures check textures n
glDrawElements check_AIOOBE indices count
glFog ifcheck params 1 pname GL_FOG_MODE,GL_FOG_DENSITY,GL_FOG_START,GL_FOG_END ifcheck params 4 pname GL_FOG_COLOR
glGenBuffers check buffers n
glGenTextures check textures n
glGetClipPlane check eqn 4
glGetIntegerv ifcheck params 1 pname GL_ALPHA_BITS,GL_ALPHA_TEST_FUNC,GL_ALPHA_TEST_REF,GL_BLEND_DST,GL_BLUE_BITS,GL_COLOR_ARRAY_BUFFER_BINDING,GL_COLOR_ARRAY_SIZE,GL_COLOR_ARRAY_STRIDE,GL_COLOR_ARRAY_TYPE,GL_CULL_FACE,GL_DEPTH_BITS,GL_DEPTH_CLEAR_VALUE,GL_DEPTH_FUNC,GL_DEPTH_WRITEMASK,GL_FOG_DENSITY,GL_FOG_END,GL_FOG_MODE,GL_FOG_START,GL_FRONT_FACE,GL_GREEN_BITS,GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES,GL_IMPLEMENTATION_COLOR_READ_TYPE_OES,GL_LIGHT_MODEL_TWO_SIDE,GL_LINE_SMOOTH_HINT,GL_LINE_WIDTH,GL_LOGIC_OP_MODE,GL_MATRIX_INDEX_ARRAY_BUFFER_BINDING_OES,GL_MATRIX_INDEX_ARRAY_SIZE_OES,GL_MATRIX_INDEX_ARRAY_STRIDE_OES,GL_MATRIX_INDEX_ARRAY_TYPE_OES,GL_MATRIX_MODE,GL_MAX_CLIP_PLANES,GL_MAX_ELEMENTS_INDICES,GL_MAX_ELEMENTS_VERTICES,GL_MAX_LIGHTS,GL_MAX_MODELVIEW_STACK_DEPTH,GL_MAX_PALETTE_MATRICES_OES,GL_MAX_PROJECTION_STACK_DEPTH,GL_MAX_TEXTURE_SIZE,GL_MAX_TEXTURE_STACK_DEPTH,GL_MAX_TEXTURE_UNITS,GL_MAX_VERTEX_UNITS_OES,GL_MODELVIEW_STACK_DEPTH,GL_NORMAL_ARRAY_BUFFER_BINDING,GL_NORMAL_ARRAY_STRIDE,GL_NORMAL_ARRAY_TYPE,GL_NUM_COMPRESSED_TEXTURE_FORMATS,GL_PACK_ALIGNMENT,GL_PERSPECTIVE_CORRECTION_HINT,GL_POINT_SIZE,GL_POINT_SIZE_ARRAY_BUFFER_BINDING_OES,GL_POINT_SIZE_ARRAY_STRIDE_OES,GL_POINT_SIZE_ARRAY_TYPE_OES,GL_POINT_SMOOTH_HINT,GL_POLYGON_OFFSET_FACTOR,GL_POLYGON_OFFSET_UNITS,GL_PROJECTION_STACK_DEPTH,GL_RED_BITS,GL_SHADE_MODEL,GL_STENCIL_BITS,GL_STENCIL_CLEAR_VALUE,GL_STENCIL_FAIL,GL_STENCIL_FUNC,GL_STENCIL_PASS_DEPTH_FAIL,GL_STENCIL_PASS_DEPTH_PASS,GL_STENCIL_REF,GL_STENCIL_VALUE_MASK,GL_STENCIL_WRITEMASK,GL_SUBPIXEL_BITS,GL_TEXTURE_BINDING_2D,GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING,GL_TEXTURE_COORD_ARRAY_SIZE,GL_TEXTURE_COORD_ARRAY_STRIDE,GL_TEXTURE_COORD_ARRAY_TYPE,GL_TEXTURE_STACK_DEPTH,GL_UNPACK_ALIGNMENT,GL_VERTEX_ARRAY_BUFFER_BINDING,GL_VERTEX_ARRAY_SIZE,GL_VERTEX_ARRAY_STRIDE,GL_VERTEX_ARRAY_TYPE,GL_WEIGHT_ARRAY_BUFFER_BINDING_OES,GL_WEIGHT_ARRAY_SIZE_OES,GL_WEIGHT_ARRAY_STRIDE_OES,GL_WEIGHT_ARRAY_TYPE_OES ifcheck params 2 pname GL_ALIASED_POINT_SIZE_RANGE,GL_ALIASED_LINE_WIDTH_RANGE,GL_DEPTH_RANGE,GL_MAX_VIEWPORT_DIMS,GL_SMOOTH_LINE_WIDTH_RANGE,GL_SMOOTH_POINT_SIZE_RANGE ifcheck params 4 pname GL_COLOR_CLEAR_VALUE,GL_COLOR_WRITEMASK,GL_SCISSOR_BOX,GL_VIEWPORT ifcheck params 16 pname GL_MODELVIEW_MATRIX,GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES,GL_PROJECTION_MATRIX,GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES,GL_TEXTURE_MATRIX,GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES ifcheck params _NUM_COMPRESSED_TEXTURE_FORMATS pname GL_COMPRESSED_TEXTURE_FORMATS,GL_FOG_COLOR,GL_LIGHT_MODEL_AMBIENT
glGetLight ifcheck params 1 pname GL_SPOT_EXPONENT,GL_SPOT_CUTOFF,GL_CONSTANT_ATTENUATION,GL_LINEAR_ATTENUATION,GL_QUADRATIC_ATTENUATION ifcheck params 3 pname GL_SPOT_DIRECTION ifcheck params 4 pname GL_AMBIENT,GL_DIFFUSE,GL_SPECULAR,GL_EMISSION
glGetMaterial ifcheck params 1 pname GL_SHININESS ifcheck params 4 pname GL_AMBIENT,GL_DIFFUSE,GL_SPECULAR,GL_EMISSION,GL_AMBIENT_AND_DIFFUSE
glGetTexEnv ifcheck params 1 pname GL_TEXTURE_ENV_MODE,GL_COMBINE_RGB,GL_COMBINE_ALPHA ifcheck params 4 pname GL_TEXTURE_ENV_COLOR
glGetTexParameter check params 1
glLightModel ifcheck params 1 pname GL_LIGHT_MODEL_TWO_SIDE ifcheck params 4 pname GL_LIGHT_MODEL_AMBIENT
glLight ifcheck params 1 pname GL_SPOT_EXPONENT,GL_SPOT_CUTOFF,GL_CONSTANT_ATTENUATION,GL_LINEAR_ATTENUATION,GL_QUADRATIC_ATTENUATION ifcheck params 3 pname GL_SPOT_DIRECTION ifcheck params 4 pname GL_AMBIENT,GL_DIFFUSE,GL_SPECULAR,GL_EMISSION
glLoadMatrix check m 16
glMaterial ifcheck params 1 pname GL_SHININESS ifcheck params 4 pname GL_AMBIENT,GL_DIFFUSE,GL_SPECULAR,GL_EMISSION,GL_AMBIENT_AND_DIFFUSE
glMultMatrix check m 16
glPointParameter check params 1
glTexEnv ifcheck params 1 pname GL_TEXTURE_ENV_MODE,GL_COMBINE_RGB,GL_COMBINE_ALPHA ifcheck params 4 pname GL_TEXTURE_ENV_COLOR
glTexImage2D nullAllowed
glTexSubImage2D nullAllowed
glBufferData nullAllowed
glTexParameter check params 1
glQueryMatrixxOES check mantissa 16 check exponent 16 return -1
glDrawTexfvOES check coords 5
glDrawTexivOES check coords 5
glDrawTexsvOES check coords 5
glDrawTexxvOES check coords 5
glBindFramebufferOES unsupported
glBindRenderbufferOES unsupported
glBlendEquation unsupported
glBlendEquationSeparate unsupported
glBlendFuncSeparate unsupported
glCheckFramebufferStatusOES unsupported return 0
glCurrentPaletteMatrixOES unsupported
glDeleteFramebuffersOES unsupported
glDeleteRenderbuffersOES unsupported
glFramebufferRenderbufferOES unsupported
glFramebufferStorageOES unsupported
glFramebufferTexture2DOES unsupported
glGenFramebuffersOES unsupported
glGenRenderbuffersOES unsupported
glGenerateMipmapOES unsupported
glGetBufferParameter unsupported
glGetFramebufferAttachmentParameterivOES unsupported
glGetRenderbufferParameterivOES unsupported
glGetTexGen unsupported
glIsFramebufferOES unsupported return JNI_FALSE
glIsRenderbufferOES unsupported return JNI_FALSE
glLoadPaletteFromModelViewMatrixOES unsupported
glMatrixIndexPointerOES unsupported
glRenderbufferStorageOES unsupported return false
glTexGen unsupported
glTexGenf unsupported
glTexGeni unsupported
glTexGenx unsupported
glWeightPointerOES unsupported
// Lots of unsupported
glAlphaFuncxOES unsupported
glBlendEquationOES unsupported
glBlendEquationSeparateOES unsupported
glBlendFuncSeparateOES unsupported
glClearColorxOES unsupported
glClearDepthfOES unsupported
glClearDepthxOES unsupported
glClipPlanefOES unsupported
glClipPlanefOES unsupported
glClipPlanexOES unsupported
glClipPlanexOES unsupported
glColor4xOES unsupported
glDepthRangefOES unsupported
glDepthRangexOES unsupported
glEGLImageTargetRenderbufferStorageOES unsupported
glEGLImageTargetTexture2DOES unsupported
glFogxOES unsupported
glFogxvOES unsupported
glFogxvOES unsupported
glFrustumfOES unsupported
glFrustumxOES unsupported
glGetClipPlanefOES unsupported
glGetClipPlanefOES unsupported
glGetClipPlanexOES unsupported
glGetClipPlanexOES unsupported
glGetFixedvOES unsupported
glGetFixedvOES unsupported
glGetLightxvOES unsupported
glGetLightxvOES unsupported
glGetMaterialxvOES unsupported
glGetMaterialxvOES unsupported
glGetTexEnvxvOES unsupported
glGetTexEnvxvOES unsupported
glGetTexGenfvOES unsupported
glGetTexGenfvOES unsupported
glGetTexGenivOES unsupported
glGetTexGenivOES unsupported
glGetTexGenxvOES unsupported
glGetTexGenxvOES unsupported
glGetTexParameterxvOES unsupported
glGetTexParameterxvOES unsupported
glLightModelxOES unsupported
glLightModelxvOES unsupported
glLightModelxvOES unsupported
glLightxOES unsupported
glLightxvOES unsupported
glLightxvOES unsupported
glLineWidthxOES unsupported
glLoadMatrixxOES unsupported
glLoadMatrixxOES unsupported
glMaterialxOES unsupported
glMaterialxvOES unsupported
glMaterialxvOES unsupported
glMultMatrixxOES unsupported
glMultMatrixxOES unsupported
glMultiTexCoord4xOES unsupported
glNormal3xOES unsupported
glOrthofOES unsupported
glOrthoxOES unsupported
glPointParameterxOES unsupported
glPointParameterxvOES unsupported
glPointParameterxvOES unsupported
glPointSizexOES unsupported
glPolygonOffsetxOES unsupported
glRotatexOES unsupported
glSampleCoveragexOES unsupported
glScalexOES unsupported
glTexEnvxOES unsupported
glTexEnvxvOES unsupported
glTexEnvxvOES unsupported
glTexGenfOES unsupported
glTexGenfvOES unsupported
glTexGenfvOES unsupported
glTexGeniOES unsupported
glTexGenivOES unsupported
glTexGenivOES unsupported
glTexGenxOES unsupported
glTexGenxvOES unsupported
glTexGenxvOES unsupported
glTexParameterxOES unsupported
glTexParameterxvOES unsupported
glTexParameterxvOES unsupported
glTranslatexOES unsupported