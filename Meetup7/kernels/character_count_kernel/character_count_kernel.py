from ipykernel.kernelbase import Kernel


class CharacterCountKernel(Kernel):
  implementation = 'CharacterCount'
  implementation_version = '1.0'
  banner = "Character count kernel - less useful than a parrot"

  language = 'no-op'
  language_version = '0.1'
  language_info = {
      'name': 'Any text',
      'mimetype': 'text/plain',
      'file_extension': '.txt',
  }

  code_character_count = 0

  def do_execute(self, code, silent, store_history=True, user_expressions=None,
                         allow_stdin=False):
    self.code_character_count += len(code)

    text_output = "Total characters in this session: {}".format(self.code_character_count)
    stream_content = {"name": "stdout", "text": text_output}
    self.send_response(self.iopub_socket, 'stream', stream_content)

    return {'status': 'ok',
      'execution_count': self.execution_count,
      'payload': [],
      'user_expressions': {},
    }


if __name__ == '__main__':
  from ipykernel.kernelapp import IPKernelApp
  IPKernelApp.launch_instance(kernel_class=CharacterCountKernel)
