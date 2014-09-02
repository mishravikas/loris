# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
import os
import zipfile
import StringIO

PROJECT_ROOT = getattr(settings, "PROJECT_ROOT", None)


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            # print newdoc
            name1 = request.FILES['docfile'].name
            print name1
            newdoc.save()
            newdoc = Document(docfile = request.FILES['docfile2'])
            print newdoc
            newdoc.save()

            #run loris.py
            os.system("python loris.py")

            # output_download(request,name1)
            # print "SENT"
            # Redirect to the document list after POST
            # return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
            name1=name1.split('.')[0]
            # fsock = open('/home/vikas/dev/loris/LORIS/Output/%s.hloris' %name1, 'r')
            # response = HttpResponse(fsock, mimetype='text/plain')
            # response['Content-Disposition'] = "attachment; filename=%s.hloris" %name1
            # return response
            # filenames = ["/home/vikas/dev/loris/LORIS/Output/%s.hloris" %name1, "/home/vikas/dev/loris/LORIS/Output/%s.vloris" %name1]
            filenames = ["%s/../../Output/%s.hloris" %(PROJECT_ROOT,name1), "%s/../../Output/%s.vloris" %(PROJECT_ROOT,name1)]

            # Folder name in ZIP archive which contains the above files
            # E.g [thearchive.zip]/somefiles/file2.txt
            # FIXME: Set this to something better
            zip_subdir = name1
            zip_filename = "%s.zip" % zip_subdir

            # Open StringIO to grab in-memory ZIP contents
            s = StringIO.StringIO()

            # The zip compressor
            zf = zipfile.ZipFile(s, "w")

            for fpath in filenames:
                # Calculate path for file in zip
                fdir, fname = os.path.split(fpath)
                zip_path = os.path.join(zip_subdir, fname)

                # Add file, at correct path
                zf.write(fpath, zip_path)

            # Must close zip for all contents to be written
            zf.close()

            # Grab ZIP file from in-memory, make response with correct MIME-type
            resp = HttpResponse(s.getvalue(), mimetype = "application/x-zip-compressed")
            # ..and correct content-disposition
            resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
            return resp
            print "HERE"
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def output_download(request,name):
    # song = .objects.get(id=song_id)
    print "recieved---------------"
    name=name.split('.')[0]
    fsock = open('/home/vikas/dev/loris/LORIS/Output/%s.hloris' %name, 'r')
    response = HttpResponse(fsock, mimetype='text/plain')
    response['Content-Disposition'] = "attachment; filename=some"
    return response

def getfiles(request):
    # Files (local path) to put in the .zip
    # FIXME: Change this (get paths from DB etc)
    filenames = ["/home/vikas/dev/loris/LORIS/Output/Sample_1.hloris", "/home/vikas/dev/loris/LORIS/Output/Sample_1.vloris"]

    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    # FIXME: Set this to something better
    zip_subdir = "somefiles"
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    s = StringIO.StringIO()

    # The zip compressor
    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), mimetype = "application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp
