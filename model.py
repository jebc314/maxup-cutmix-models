import torchvision.models as models

from torch import nn


def init_model(num_classes=10):
    model = models.resnet50(pretrained=True) # MODIFICATION-Changed to resnet50
    model.avgpool = nn.AdaptiveAvgPool2d(1)
    model.fc = nn.Sequential(
        nn.BatchNorm1d(2048, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True), # MODIFICATION-changed to 2048
        nn.Linear(in_features=2048, out_features=num_classes, bias=True), # MODIFICATION-changed to 2048
    )
    return model
