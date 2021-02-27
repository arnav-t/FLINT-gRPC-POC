FROM mojaglobal/flint

WORKDIR /server

COPY app.py Makefile ./
ADD proto/* proto/

EXPOSE 50051

RUN python3 -m pip install --upgrade pip && \ 
python3 -m pip install --upgrade setuptools
RUN make install && make

CMD ["python3", "app.py"]