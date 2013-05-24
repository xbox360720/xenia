# Copyright 2013 Ben Vanik. All Rights Reserved.
{
  'targets': [
    {
      'target_name': 'asmjit',
      'type': '<(library)',

      'direct_dependent_settings': {
        'include_dirs': [
          'asmjit/src/',
        ],
        'defines': [
          'ASMJIT_X64=',
          'ASMJIT_API=',
        ],
      },

      'defines': [
        'ASMJIT_X64=',
        'ASMJIT_API=',
      ],

      'include_dirs': [
        'asmjit/src/',
      ],

      'sources': [
        'asmjit/src/asmjit/asmjit.h',
        'asmjit/src/asmjit/config.h',
        'asmjit/src/asmjit/core.h',
        'asmjit/src/asmjit/x86.h',
        'asmjit/src/asmjit/core/apibegin.h',
        'asmjit/src/asmjit/core/apiend.h',
        'asmjit/src/asmjit/core/assembler.cpp',
        'asmjit/src/asmjit/core/assembler.h',
        'asmjit/src/asmjit/core/assert.cpp',
        'asmjit/src/asmjit/core/assert.h',
        'asmjit/src/asmjit/core/buffer.cpp',
        'asmjit/src/asmjit/core/buffer.h',
        'asmjit/src/asmjit/core/build.h',
        'asmjit/src/asmjit/core/compiler.cpp',
        'asmjit/src/asmjit/core/compiler.h',
        'asmjit/src/asmjit/core/compilercontext.cpp',
        'asmjit/src/asmjit/core/compilercontext.h',
        'asmjit/src/asmjit/core/compilerfunc.cpp',
        'asmjit/src/asmjit/core/compilerfunc.h',
        'asmjit/src/asmjit/core/compileritem.cpp',
        'asmjit/src/asmjit/core/compileritem.h',
        'asmjit/src/asmjit/core/context.cpp',
        'asmjit/src/asmjit/core/context.h',
        'asmjit/src/asmjit/core/cpuinfo.cpp',
        'asmjit/src/asmjit/core/cpuinfo.h',
        'asmjit/src/asmjit/core/defs.cpp',
        'asmjit/src/asmjit/core/defs.h',
        'asmjit/src/asmjit/core/func.cpp',
        'asmjit/src/asmjit/core/func.h',
        'asmjit/src/asmjit/core/intutil.h',
        'asmjit/src/asmjit/core/lock.h',
        'asmjit/src/asmjit/core/logger.cpp',
        'asmjit/src/asmjit/core/logger.h',
        'asmjit/src/asmjit/core/memorymanager.cpp',
        'asmjit/src/asmjit/core/memorymanager.h',
        'asmjit/src/asmjit/core/memorymarker.cpp',
        'asmjit/src/asmjit/core/memorymarker.h',
        'asmjit/src/asmjit/core/operand.cpp',
        'asmjit/src/asmjit/core/operand.h',
        'asmjit/src/asmjit/core/podvector.h',
        'asmjit/src/asmjit/core/stringbuilder.cpp',
        'asmjit/src/asmjit/core/stringbuilder.h',
        'asmjit/src/asmjit/core/stringutil.cpp',
        'asmjit/src/asmjit/core/stringutil.h',
        'asmjit/src/asmjit/core/virtualmemory.cpp',
        'asmjit/src/asmjit/core/virtualmemory.h',
        'asmjit/src/asmjit/core/zonememory.cpp',
        'asmjit/src/asmjit/core/zonememory.h',
        'asmjit/src/asmjit/x86/x86assembler.cpp',
        'asmjit/src/asmjit/x86/x86assembler.h',
        'asmjit/src/asmjit/x86/x86compiler.cpp',
        'asmjit/src/asmjit/x86/x86compiler.h',
        'asmjit/src/asmjit/x86/x86compilercontext.cpp',
        'asmjit/src/asmjit/x86/x86compilercontext.h',
        'asmjit/src/asmjit/x86/x86compilerfunc.cpp',
        'asmjit/src/asmjit/x86/x86compilerfunc.h',
        'asmjit/src/asmjit/x86/x86compileritem.cpp',
        'asmjit/src/asmjit/x86/x86compileritem.h',
        'asmjit/src/asmjit/x86/x86cpuinfo.cpp',
        'asmjit/src/asmjit/x86/x86cpuinfo.h',
        'asmjit/src/asmjit/x86/x86defs.cpp',
        'asmjit/src/asmjit/x86/x86defs.h',
        'asmjit/src/asmjit/x86/x86func.cpp',
        'asmjit/src/asmjit/x86/x86func.h',
        'asmjit/src/asmjit/x86/x86operand.cpp',
        'asmjit/src/asmjit/x86/x86operand.h',
        'asmjit/src/asmjit/x86/x86util.cpp',
        'asmjit/src/asmjit/x86/x86util.h',
      ],
    }
  ]
}
