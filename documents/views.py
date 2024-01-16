import markdown
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from .forms import EditDocumentForm


def home(request):
    new_doc = Document.objects.create()
    form = EditDocumentForm()
    return render(request, "documents/edit.html", {"form":form, "doc":new_doc} )
    # return redirect("documents:edit_documents")

@require_http_methods(['GET', 'POST'])
def edit_document(request, docref):
    doc = get_object_or_404(Document, ref=docref)
    form = EditDocumentForm(request.POST or None, instance=doc)
    if request.method == "POST":
        if form.is_valid():
            doc = form.save()
        else:
            messages = ["There are errors in form!"]
            return render(request, "documents/edit.html", {"form":form, "doc":doc, "messages":messages} )
        return render(request, "documents/edit.html", {"form":form, "doc":doc} )

    # return redirect("documents:home")

def render_document(request, docref):
    doc = get_object_or_404(Document, ref=docref)
    markdown_contents = markdown.markdown(doc.contents)
    return render(request, "documents/render.html", {"doc":doc, "markdown_contents":markdown_contents})
